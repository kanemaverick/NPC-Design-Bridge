# 游戏角色立绘提示词工程参考

## 一、英文 Prompt 结构规范

### 标准结构（按权重从高到低排列）

```
[质量前缀] + [主体描述] + [面部特征] + [服装道具] + [姿态构图] + [背景氛围] + [风格技法] + [质量后缀]
```

### 质量前缀（必选）

放在最前面，提升整体生成质量：

```
masterpiece, best quality, ultra-detailed, [作品类型],
```

### 主体描述（最重要）

```
[年龄] [种族/地域] [性别], [体型], [核心气质]
```

| 中文描述 | 英文对应 |
|---------|---------|
| 年轻女性 | young woman, youthful |
| 中年男性 | middle-aged man, mature |
|  elderly | elderly, aged, old |
| 儿童 | child, young boy/girl |
| 东亚 | East Asian, Chinese, Japanese, Korean |
| 欧美 | Caucasian, European, Western |
| 壮硕 | muscular, athletic build, strong |
| 纤细 | slender, slim, petite |
| 丰满 | plump, curvy, full-figured |
| 高挑 | tall, statuesque, long-legged |
| 矮小 | short, petite, small stature |

### 面部特征

```
[表情], [眼睛], [发型], [面部标志]
```

| 特征 | 英文描述 |
|-----|---------|
| 温柔微笑 | gentle smile, warm expression, soft gaze |
| 冷淡 | cold expression, aloof gaze, emotionless face |
| 神秘 | mysterious smile, enigmatic expression, piercing eyes |
| 锐利眼神 | sharp eyes, intense gaze, piercing look |
| 下垂眼 | droopy eyes, gentle eye shape, downcast gaze |
| 细长眼 | slender eyes, narrow eyes, fox-like eyes |
| 大眼睛 | large expressive eyes, doe eyes, wide eyes |
| 单马尾 | ponytail, high ponytail, low ponytail |
| 双马尾 | twin tails, pigtails, twin drills |
| 短发 | short hair, bob cut, pixie cut |
| 长发 | long flowing hair, waist-length hair |
| 卷发 | curly hair, wavy hair, ringlets |
| 直发 | straight hair, sleek hair |
| 刘海 | bangs, fringe, side-swept bangs |
| 眼镜 | glasses, round glasses, rimless glasses, spectacles |
| 面纱 | veil, half-mask, blindfold |
| 伤疤 | scar, facial scar, scar across cheek |
| 雀斑 | freckles, light freckles across nose |

### 发色与瞳色

| 颜色 | 英文（可叠加描述）|
|-----|------------------|
| 银白 | silver hair, white hair, platinum blonde |
| 金色 | golden hair, blonde, honey blonde |
| 黑色 | black hair, jet black, dark hair |
| 棕色 | brown hair, chestnut brown, auburn |
| 红色 | red hair, crimson, scarlet, burgundy |
| 蓝色 | blue hair, azure, sky blue, navy blue |
| 紫色 | purple hair, violet, lavender, amethyst |
| 粉色 | pink hair, pastel pink, rose pink |
| 异色瞳 | heterochromia, different colored eyes, one blue one gold |
| 金色眼 | golden eyes, amber eyes, honey-colored eyes |
| 红色眼 | red eyes, crimson eyes, blood-red eyes |
| 蓝色眼 | blue eyes, sapphire eyes, ocean blue eyes |
| 绿色眼 | green eyes, emerald eyes, jade eyes |
| 灰色眼 | gray eyes, silver eyes, steel gray eyes |

### 服装与道具

```
[服装类型] + [颜色/材质] + [标志性道具]
```

| 服装类型 | 英文描述 |
|---------|---------|
| 旗袍 | qipao, cheongsam, traditional Chinese dress |
| 和服 | kimono, traditional Japanese clothing, yukata |
| 汉服 | hanfu, traditional Chinese hanfu |
| 西装 | suit, blazer, business suit, formal attire |
| 盔甲 | armor, plate armor, knight armor, samurai armor |
| 法师袍 | mage robe, wizard cloak, sorcerer's gown, flowing robes |
| 冒险者装 | adventurer's outfit, traveler's clothes, leather armor |
| 女仆装 | maid outfit, victorian maid dress, frilly apron |
| 军装 | military uniform, officer's uniform, combat gear |
| 休闲装 | casual clothes, hoodie, jeans, t-shirt |
| 礼服 | evening gown, formal dress, ball gown, cocktail dress |
| 围裙 | apron, work apron, floral apron, kitchen apron |
| 斗篷 | cloak, cape, hooded cloak, tattered cape |
| 外套 | coat, trench coat, fur coat, overcoat |
| 连衣裙 | dress, sundress, floral dress, maxi dress |
| 衬衫 | shirt, blouse, button-up shirt, collared shirt |
| 高领 | turtleneck, high-neck, mock neck |
| 背心 | vest, waistcoat, sleeveless top, tank top |
| 短裤 | shorts, hot pants, denim shorts |
| 长裙 | long skirt, maxi skirt, flowing skirt |
| 短裙 | short skirt, mini skirt, pleated skirt |
| 靴子 | boots, knee-high boots, leather boots, combat boots |
| 高跟鞋 | high heels, stilettos, pumps |
| 平底鞋 | flats, loafers, sandals, slippers |

| 道具/配件 | 英文描述 |
|----------|---------|
| 武器 | sword, katana, staff, wand, bow, gun, dagger |
| 书本 | book, tome, spellbook, ancient book |
| 茶具 | teapot, tea cup, tea set, clay teapot |
| 法器 | orb, crystal ball, magical artifact, amulet |
| 乐器 | lyre, flute, violin, harp, lute |
| 工具 | hammer, wrench, toolkit, crafting tools |
| 食物 | bread, apple, bento, cake, onigiri |
| 动物 | cat, dog, bird, owl, fox companion, familiar |
| 背包 | backpack, traveler's bag, satchel, messenger bag |
| 饰品 | necklace, earrings, bracelet, ring, brooch, hairpin |
| 帽子 | hat, beret, wide-brimmed hat, top hat, straw hat |
| 围巾 | scarf, shawl, neckerchief, muffler |
| 手套 | gloves, fingerless gloves, lace gloves, leather gloves |
| 腰带 | belt, sash, utility belt, ornate belt |
| 眼镜 | glasses, monocle, goggles, sunglasses |
| 面具 | mask, half-mask, theatrical mask, carnival mask |

### 姿态与构图

```
[姿态] + [手部动作] + [视角/构图]
```

| 姿态 | 英文描述 |
|-----|---------|
| 站立 | standing, upright posture, standing confidently |
| 坐姿 | sitting, sitting on a chair, sitting cross-legged, sitting on the ground |
| 行走 | walking, striding, mid-stride, walking forward |
| 战斗 | battle stance, fighting pose, ready to fight, combat pose |
| 休息 | leaning against wall, resting, relaxed posture, lounging |
| 奔跑 | running, sprinting, dashing |
| 跳跃 | jumping, mid-air, leaping |
| 跪姿 | kneeling, kneeling on one knee, prostrating |
| 倚靠 | leaning, leaning on a cane, leaning against a table |
| 双手抱胸 | arms crossed, crossing arms, folded arms |
| 手插口袋 | hands in pockets, one hand in pocket |
| 手持物品 | holding [item], carrying [item], wielding [item] |
| 抚摸 | petting, stroking, gently touching |
| 托腮 | resting chin on hand, hand on cheek, thoughtful pose |
| 招手 | waving, beckoning, gesturing |
| 祈祷 | praying, hands clasped, meditating |
| 阅读 | reading, holding a book, flipping pages |
| 品茶 | sipping tea, holding a tea cup, tea ceremony |
| 施法 | casting spell, magic gesture, spellcasting pose, channeling mana |
| 演奏 | playing instrument, strumming, bowing violin |

| 视角 | 英文描述 |
|-----|---------|
| 正面 | front view, facing viewer, frontal portrait |
| 侧面 | side view, profile view, side profile |
| 四分之三 | three-quarter view, 3/4 view, turning slightly |
| 背面 | back view, from behind, rear view |
| 仰视 | low angle shot, looking up at character, heroic angle |
| 俯视 | high angle shot, looking down, bird's eye view |
| 平视 | eye level, neutral angle |
| 特写 | close-up, portrait shot, face close-up |
| 半身 | half-body, upper body, bust shot |
| 全身 | full body, full length, standing figure |
| 角色卡 | character card UI, character sheet, game UI frame, profile card |
| 立绘 | character illustration, standing illustration, character art |
| 概念图 | concept art, character concept, design sheet |

### 背景与氛围

```
[环境] + [光影] + [色调] + [氛围/情绪]
```

| 环境 | 英文描述 |
|-----|---------|
| 室内 | interior, room, inside, indoor setting |
| 室外 | outdoor, outside, open air, nature |
| 茶馆 | tea house, traditional tea room, Japanese tea house |
| 酒馆 | tavern, inn, pub, bar, medieval tavern |
| 商店 | shop, store, marketplace, bazaar, shop interior |
| 书房 | study, library, book-filled room, scholar's chamber |
| 卧室 | bedroom, cozy room, sleeping quarters |
| 厨房 | kitchen, cooking area, rustic kitchen |
| 花园 | garden, flower garden, botanical garden, zen garden |
| 森林 | forest, woods, deep forest, enchanted forest |
| 城市 | city, urban background, street scene, cityscape |
| 村庄 | village, rural setting, countryside, small town |
| 废墟 | ruins, ancient ruins, crumbling architecture, destroyed city |
| 城堡 | castle, fortress, palace, grand hall, throne room |
| 塔楼 | tower, wizard's tower, bell tower, clock tower |
| 洞穴 | cave, cavern, underground, crystal cave |
| 海边 | seaside, beach, ocean, coast, shoreline |
| 山脉 | mountain, mountain peak, alpine, cliffside |
| 雪地 | snow, snowy landscape, winter scene, blizzard |
| 沙漠 | desert, sand dunes, oasis, arid landscape |
| 太空 | space, cosmic background, starfield, nebula |
| 赛博 | cyberpunk city, neon-lit street, futuristic cityscape, holographic ads |
| 蒸汽朋克 | steampunk, brass gears, Victorian machinery, clockwork |

| 光影 | 英文描述 |
|-----|---------|
| 暖光 | warm light, golden hour lighting, warm sunlight, soft warm glow |
| 冷光 | cool light, blue lighting, cold light, moonlight |
| 侧光 | side lighting, rim lighting, edge lighting |
| 背光 | backlighting, silhouette, halo effect, backlit |
| 顶光 | overhead lighting, top lighting, dramatic top light |
| 底光 | underlighting, upward lighting, eerie underlighting |
| 柔光 | soft light, diffused lighting, gentle lighting, ambient light |
| 硬光 | hard light, harsh lighting, strong shadows, direct light |
| 点光 | spotlight, focused light, beam of light, single light source |
| 自然光 | natural lighting, daylight, sunlight, outdoor lighting |
| 烛光 | candlelight, warm flickering light, firelight, torchlight |
| 魔法光 | magical glow, ethereal light, mystical aura, shimmering light |
| 霓虹光 | neon lighting, neon glow, fluorescent light, cyberpunk lighting |
| 体积光 | volumetric lighting, god rays, light rays, atmospheric lighting |
| 黄昏 | sunset, dusk, twilight, golden hour, evening light |
| 黎明 | dawn, sunrise, early morning light, first light |
| 夜晚 | night, nighttime, dark, moonlit, starlit |
| 阴天 | overcast, cloudy, diffused daylight, gray sky |
| 雾中 | foggy, misty, hazy, atmospheric fog, morning mist |
| 雨中 | raining, rainy, wet, rain droplets, wet surfaces |
| 雪中 | snowing, snowy, winter atmosphere, falling snow |

| 色调/氛围 | 英文描述 |
|----------|---------|
| 暖色调 | warm color palette, warm tones, orange and amber, cozy colors |
| 冷色调 | cool color palette, cool tones, blue and silver, cold colors |
| 高饱和 | vibrant colors, saturated colors, bright and vivid, colorful |
| 低饱和 | muted colors, desaturated, pastel colors, soft tones |
| 单色 | monochromatic, single color scheme, limited palette |
| 互补色 | complementary colors, contrasting colors, color contrast |
| 赛博朋克配色 | neon colors, cyberpunk palette, cyan and magenta, electric colors |
| 自然配色 | earthy tones, natural colors, green and brown, organic palette |
| 金属感 | metallic colors, silver and gold, chrome, iridescent |
| 梦幻感 | dreamy atmosphere, ethereal, whimsical, magical atmosphere |
| 恐怖感 | horror atmosphere, dark and eerie, ominous, unsettling |
| 治愈感 | healing atmosphere, cozy and warm, comforting, peaceful |
| 史诗感 | epic atmosphere, grand and majestic, heroic, monumental |
| 神秘感 | mysterious atmosphere, enigmatic, secretive, arcane |
| 科技感 | sci-fi atmosphere, high-tech, futuristic, sleek |
| 复古感 | vintage atmosphere, retro, nostalgic, old-fashioned |
| 废墟感 | post-apocalyptic, dystopian, ruined, decaying |

### 风格与技法

```
[画风] + [渲染/技法] + [参考作品/艺术家] + [质量后缀]
```

| 画风 | 英文描述 |
|-----|---------|
| 二次元 | anime style, Japanese anime, manga style, anime game art |
| 写实 | photorealistic, realistic, lifelike, hyperrealistic |
| 半写实 | semi-realistic, realistic anime, 2.5D, realistic illustration |
| 卡通 | cartoon style, stylized cartoon, western cartoon, chibi |
| 欧美卡渲 | stylized 3D, toon shading, cel-shaded 3D, game art style |
| 像素 | pixel art, 16-bit, 8-bit, retro pixel style, pixelated |
| 水墨 | ink wash painting, sumi-e, Chinese brush painting, traditional East Asian painting |
| 赛博朋克 | cyberpunk art, neon noir, futuristic digital art, high-tech low-life |
| 蒸汽朋克 | steampunk art, Victorian sci-fi, brass and gears, clockwork aesthetic |
| 低多边形 | low poly, low-poly 3D, geometric, faceted, minimalist 3D |
| 吉卜力 | Ghibli style, Studio Ghibli-inspired, Hayao Miyazaki style, warm anime |
| 新海诚 | Makoto Shinkai style, detailed anime background, luminous sky, dramatic clouds |
| 原神风格 | Genshin Impact style, anime game character, HoYoverse style, fantasy anime |
| 碧蓝幻想 | Granblue Fantasy style, Cygames anime art, elaborate fantasy anime |
| FGO风格 | Fate/Grand Order style, TYPE-MOON anime, detailed line art, ornate design |
|  Arcane风格 | Arcane style, League of Legends animation, painted texture, stylized realism |
| 迪士尼 | Disney style, Disney animation, classic animation, expressive cartoon |
| 皮克斯 | Pixar style, 3D animation, Pixar-like rendering, appealing cartoon |
| 复古海报 | vintage poster style, art nouveau, retro illustration, propaganda poster style |
| 波普艺术 | pop art, Andy Warhol style, bold colors, comic book style |
| 油画 | oil painting, classical oil painting, baroque painting, Renaissance style |
| 水彩 | watercolor, watercolour painting, wet-on-wet, transparent washes |
| 素描 | pencil sketch, graphite drawing, line drawing, cross-hatching |
| 版画 | woodcut print, linocut, screen print, block print style |
| 概念艺术 | concept art, game concept art, character concept, design illustration |
| 视觉小说 | visual novel style, VN art, dating sim art, galgame style |
| 偶像大师 | Idolmaster style, Bandai Namco anime, bright idol anime, sparkly |
| 东方Project | Touhou Project style, ZUN art style, danmaku game art, bullet hell aesthetic |
| 最终幻想 | Final Fantasy style, Square Enix character design, Tetsuya Nomura style, JRPG art |
| 宝可梦 | Pokemon style, Ken Sugimori style, monster design, friendly creature design |
| 塞尔达 | Zelda style, Breath of the Wild style, cel-shaded fantasy, Nintendo art |
| 马里奥 | Mario style, Nintendo character design, cheerful cartoon, bright and friendly |
| 黑暗之魂 | Dark Souls style, FromSoftware aesthetic, dark fantasy, gothic medieval |
| 艾尔登法环 | Elden Ring style, George R.R. Martin fantasy, dark grandeur, majestic decay |
| 巫师3 | Witcher 3 style, Slavic fantasy, dark realism, gritty medieval |
| 荒野大镖客 | Red Dead Redemption style, Western realism, cinematic cowboy, American frontier |
| 死亡搁浅 | Death Stranding style, Kojima aesthetic, surreal sci-fi, lonely epic |

| 渲染/技法 | 英文描述 |
|----------|---------|
| 线条干净 | clean linework, smooth lines, crisp outlines, defined edges |
| 线条 rough | rough linework, sketchy lines, expressive strokes, gestural lines |
| 赛璐璐 | cel-shading, toon shading, flat shading, anime shading |
| 软渲染 | soft shading, airbrush style, gradient shading, smooth rendering |
| 厚涂 | thick paint, impasto, painterly style, heavy brushstrokes |
| 平涂 | flat colors, flat shading, minimal shading, graphic style |
| 半厚涂 | semi-rendered, soft cel-shading, anime painting style |
| 3D渲染 | 3D render, CGI, rendered, 3D model, digital sculpture |
| 手绘感 | hand-drawn feel, traditional media look, organic texture |
| 照片感 | photographic, photo-like, camera-like, photorealistic rendering |
| 电影感 | cinematic, film-like, cinematic composition, movie poster style |
| 8K超清 | 8k uhd, ultra high resolution, highly detailed, sharp details |
| 精细细节 | intricate details, elaborate details, fine details, highly detailed |
| 大场景 | wide shot, grand scenery, epic scale, vast landscape |
| 特写 | close-up, macro shot, detailed close-up, extreme close-up |
| 动态模糊 | motion blur, speed lines, dynamic movement, action blur |
| 景深 | depth of field, bokeh, shallow depth of field, background blur |
| 粒子效果 | particle effects, floating particles, dust motes, magical sparkles |
| 发光效果 | glowing effects, bloom, luminous, radiant light, ethereal glow |
| 反射 | reflections, shiny surfaces, reflective materials, mirror-like |
| 半透明 | translucent, semi-transparent, see-through, glass-like |
| 金属质感 | metallic texture, metal sheen, chrome finish, polished metal |
| 布料质感 | fabric texture, cloth folds, drapery, flowing fabric |
| 皮肤质感 | skin texture, pores, subsurface scattering, realistic skin |
| 毛发质感 | fur texture, hair strands, realistic hair, flowing hair |
| 鳞片质感 | scales texture, scaly skin, reptilian texture, dragon scales |

| 质量后缀 | 英文描述 |
|---------|---------|
| 必加 | masterpiece, best quality, ultra-detailed, highres, 8k uhd |
| 推荐 | official art, professional artwork, trending on artstation, pixiv, deviantart |
| 可选 | wallpaper, cover art, splash art, key visual, promotional art |

### 负面提示词（Negative Prompt）模板

标准模板（适用于大部分画风）：

```
(worst quality, low quality, normal quality:1.4), lowres, bad anatomy, bad hands, 
text, watermark, signature, username, artist name, error, cropped, jpeg artifacts, 
ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, 
poorly drawn hands, poorly drawn face, mutation, deformed, extra limbs, 
extra arms, extra legs, fused fingers, too many fingers, long neck, 
cross-eyed, blurry, bad feet, mutated, poorly drawn, bad proportions, 
missing arms, missing legs, extra foot, bad knee, extra knees, more than 2 legs, 
more than 2 arms, malformed limbs, missing fingers, bad hand, bad fingers, 
liquid hand, liquid body, poorly drawn body, text, logo, watermark, signature, 
monochrome, greyscale, amateur, 3d render, sketch, cartoon, anime, manga, 
nsfw, nude, naked, topless, bottomless, underwear, lingerie, bikini, 
bare shoulders, bare chest, cleavage, see-through, revealing clothes, 
blood, gore, violence, death, corpse, dismembered, scary, horror, 
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, 
fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, 
signature, watermark, username, blurry, artist name, bad_prompt, bad-artist, 
bad-hands-5, badhandv4, EasyNegative, ng_deepnegative_v1_75t, verybadimagenegative_v1.3
```

**针对特定画风的调整**：

- **二次元**：增加 `3d, realistic, photorealistic, western cartoon, 3d render, cgi`
- **写实**：增加 `anime, cartoon, manga, 2d, flat colors, cel-shading`
- **卡通**：增加 `realistic, photorealistic, anime, manga, 3d render`
- **像素**：增加 `smooth, anti-aliased, high resolution, realistic, 3d`
- **水墨**：增加 `colorful, vibrant, saturated, western style, oil painting, anime`

## 二、游戏类型与视觉调性对照表

| 游戏类型 | 视觉调性关键词 | 推荐画风 | 色调建议 | 光影建议 |
|---------|--------------|---------|---------|---------|
| 治愈经营 | cozy, gentle, heartwarming, peaceful, everyday life | 二次元/水彩/吉卜力 | 暖色为主（橙、黄、绿），低对比 | 柔光、自然光、暖光 |
| RPG冒险 | epic, adventurous, heroic, fantasy, grand | 二次元/半写实/概念艺术 | 中高饱和，冷暖对比 | 戏剧性光影、体积光、魔法光 |
| 恐怖悬疑 | dark, eerie, mysterious, unsettling, gothic | 写实/暗黑二次元/哥特 | 低饱和，暗色为主，突兀高亮 | 硬光、侧光、底光、阴影 |
| 科幻/赛博 | futuristic, high-tech, neon, cybernetic, dystopian | 赛博朋克/硬科幻/低多边 | 霓虹色（青、品红、紫），高对比 | 多光源、霓虹光、全息投影光 |
| 解谜/探索 | intellectual, curious, ancient, puzzle-like, mysterious | 二次元/水墨/概念艺术 | 中等饱和，偏冷或偏暖视主题 | 点光、体积光、神秘光 |
| 模拟/沙盒 | diverse, modular, creative, sandbox, colorful | 卡通/像素/多元风格 | 鲜明色块，高识别度配色 | 均匀光、明亮光、卡通光 |
| 格斗/动作 | dynamic, intense, action-packed, powerful, fast | 二次元/欧美卡渲/写实 | 高饱和，强烈色彩对比 | 动态光、速度线、冲击光 |
| 恋爱/视觉小说 | romantic, emotional, beautiful, expressive, dramatic | 二次元/视觉小说/水彩 | 柔和色，粉色/蓝色系，梦幻感 | 柔光、逆光、梦幻光 |
| 策略/战棋 | tactical, strategic, military, historical, grand | 写实/半写实/历史风格 | 沉稳色，军绿/棕/灰，低饱和 | 顶光、硬光、戏剧性光 |
| 肉鸽/地牢 | dungeon, rogue-like, dark fantasy, perilous, loot | 暗黑二次元/像素/写实 | 暗色为主，宝箱/魔法有亮色点缀 | 点光、 torchlight、暗环境 |

## 三、常见角色类型的视觉记忆点（Signature）

| 角色类型 | 视觉记忆点建议 |
|---------|-------------|
| 老奶奶/老爷爷 | 标志性眼镜、特定发型（发髻/辫子）、永远拿着的道具（茶壶/拐杖/书） |
| 商人/店主 | 标志性服饰元素（围裙/华丽外衣）、永远算着的算盘/账本、特定的帽子 |
| 骑士/战士 | 标志性盔甲部件（肩甲/头盔）、标志性武器（ oversized sword）、披风颜色 |
| 法师/巫师 | 标志性法器（法杖/水晶球/书）、标志性的魔法光效颜色、长袍上的特定符号 |
| 刺客/盗贼 | 标志性面具/面罩、标志性武器（双匕首/短剑）、特定的姿势（蹲伏/阴影中） |
| 医生/治疗者 | 标志性的医疗道具（药瓶/绷带/权杖）、特定的配色（白+绿/蓝）、温和的表情 |
| 机械师/工程师 | 标志性的工具（扳手/护目镜/机械臂）、油污/机油痕迹、特定的工装 |
| 歌手/艺人 | 标志性的乐器/麦克风、特定的舞台服装、标志性的发型/妆容 |
| 厨师/料理人 | 标志性的厨师帽/围裙、永远拿着的锅铲/食材、特定的体型特征 |
| 学者/图书管理员 | 标志性的眼镜、永远抱着的书/卷轴、特定的长袍/制服 |

## 四、Prompt 调优技巧

### 1. 权重控制（Weighted Prompts）

在 Stable Diffusion 等模型中，可用括号控制权重：

```
(masterpiece:1.2), (best quality:1.2), (detailed face:1.3), (red eyes:1.1)
```

- 默认值：1.0
- 强调：1.1-1.3
- 核心特征：1.3-1.5
- 弱化：0.8-0.9

### 2. 关键词顺序

AI 对 prompt 开头部分权重更高：

1. 质量词（masterpiece, best quality）
2. 主体（角色核心描述）
3. 面部特征（最重要的人物识别点）
4. 服装/道具
5. 姿态/构图
6. 背景
7. 风格/质量后缀

### 3. 避免的问题

| 问题 | 解决方式 |
|-----|---------|
| 描述矛盾 | 统一风格（不写"写实动漫"），选其一或说"半写实" |
| 过于笼统 | 用具体形容词替换模糊词（"好看"→"精致五官+柔和光线+暖色调"） |
| 中式英语 | 不用直译，用英文游戏美术术语（如不用"old and kind woman"，用"elderly gentlewoman"） |
| 过长导致截断 | 控制在 150 词以内，核心特征前置 |
| 忽略负面提示 | 始终提供完整的负面 prompt，尤其要去掉 text/watermark/bad anatomy |
| 角色不像游戏立绘 | 明确加入"game character portrait/character illustration/character design sheet" |

### 4. 迭代优化策略

当生图结果不理想时：

1. **整体不像** → 调整风格词和渲染词（换画风或质量后缀）
2. **面部不对** → 强化面部描述（增加详细形容词、调权重）
3. **服装不对** → 细化服装材质和颜色描述
4. **背景太乱** → 简化背景描述或增加"simple background/blurred background"
5. **姿态不对** → 明确指定 pose 词，增加视角描述
6. **质量太低** → 强化质量前缀，增加"8k uhd, highly detailed, sharp focus"
7. **有文字/水印** → 在负面提示词中增加`(text, watermark, signature:1.5)`

## 五、快速查询表

### 生图参数速查

| 参数 | 推荐值 | 说明 |
|-----|-------|------|
| 尺寸（竖版立绘） | 1024x1536 | 适合全身/半身角色立绘 |
| 尺寸（横版场景） | 1536x1024 | 适合带场景的角色图 |
| 尺寸（正方形） | 1024x1024 | 适合头像/胸像 |
| 步数（Steps） | 30-50 | 越高细节越多，但速度越慢 |
| CFG Scale | 7-9 | 越高 prompt 遵循度越高，但可能过饱和 |
| 采样器 | DPM++ 2M Karras / Euler a | 通用推荐 |
| 模型 | gpt-image-2 / DALL-E 3 / SDXL / Niji | 根据画风选择 |
| 质量 | high / best quality | 在 prompt 中也要强调 |

### 画风快速选择

| 用户说 | 推荐画风 | 关键词 |
|-------|---------|--------|
| "二次元" | 日式动漫 | anime style, Japanese game art, cel-shading |
| "像原神" | 原神风格 | Genshin Impact style, HoYoverse anime |
| "像 Arcane" | Arcane风格 | Arcane style, painted texture, stylized realism |
| "像迪士尼" | 迪士尼风格 | Disney style, expressive cartoon, appealing design |
| "写实" | 写实渲染 | photorealistic, cinematic lighting, detailed skin |
| "像素" | 像素风格 | pixel art, 16-bit, retro game aesthetic |
| "水墨" | 水墨风格 | Chinese ink wash painting, sumi-e, brush strokes |
| "赛博朋克" | 赛博朋克 | cyberpunk, neon lights, futuristic city |
| "Q版" | 卡通/SD | chibi, super deformed, cute cartoon style |
| "复古" | 复古风格 | vintage style, retro illustration, art nouveau |

