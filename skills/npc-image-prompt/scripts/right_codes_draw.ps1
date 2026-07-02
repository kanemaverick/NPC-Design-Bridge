param(
  [Parameter(Mandatory = $true)]
  [string]$Prompt,

  [string]$Size = "auto",
  [string]$Model = "gpt-image-2",
  [int]$N = 1,
  [string]$Quality = "auto",
  [string]$OutputFormat = "png",
  [string]$Background = "auto",
  [string]$Moderation = "auto",
  [int]$MaxAttempts = 3,
  [int]$RetryDelaySec = 8,
  [string]$BaseUrl = "https://www.right.codes/draw",
  [string]$ApiKey = $env:RIGHT_CODES_DRAW_API_KEY
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ApiKey)) {
  throw "RIGHT_CODES_DRAW_API_KEY is required. Set it in the environment or pass -ApiKey explicitly."
}

$uri = ($BaseUrl.TrimEnd("/") + "/v1/images/generations")
$headers = @{
  Authorization = "Bearer $ApiKey"
  "Content-Type" = "application/json"
}

$body = @{
  model = $Model
  prompt = $Prompt
  n = $N
  size = $Size
  quality = $Quality
  output_format = $OutputFormat
  background = $Background
  moderation = $Moderation
} | ConvertTo-Json -Depth 8

$lastError = $null

for ($attempt = 1; $attempt -le $MaxAttempts; $attempt++) {
  try {
    $response = Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -Body $body -TimeoutSec 180
    $response | ConvertTo-Json -Depth 12
    exit 0
  } catch {
    $statusCode = $null
    if ($_.Exception.Response -and $_.Exception.Response.StatusCode) {
      $statusCode = [int]$_.Exception.Response.StatusCode
    }

    $lastError = [ordered]@{
      ok = $false
      provider = "right-codes-draw"
      attempt = $attempt
      max_attempts = $MaxAttempts
      status = $statusCode
      message = $_.Exception.Message
      detail = $_.ErrorDetails.Message
    }

    if (($statusCode -in @(502, 503, 504)) -and $attempt -lt $MaxAttempts) {
      Start-Sleep -Seconds $RetryDelaySec
      continue
    }

    break
  }
}

$lastError | ConvertTo-Json -Depth 8
exit 1
