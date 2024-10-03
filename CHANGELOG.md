# Changelog

All notable changes to this project will be documented in this file.

**Note:** All dates are recorded in Beijing Time (CST).

## Version 0.0.0 - 2024-06-11-18:00

**Come up with an idea**：双人贪吃蛇对战。

Idea 的到来源于期末周除了复习以外的所有事物都变得十分有趣。并且当时忘记了贪吃蛇大作战这类游戏的存在，以为自己创意十足。

## Version 1.1.0 - 2024-06-12-17:00

### Added

- 初步搭建游戏框架，具备最简单的单人游戏功能。

## Version 1.1.1 - 2024-06-12-18:00

### Added

- 增加记录最高分的功能。

## Version 1.2.0 - 2024-06-12-22:30

### Added

- 增加了双人模式
- 增加游戏开始前的交互与模式选择

### Fixed

- 修复了快速掉头直接死亡的bug
- 修复了点的生成可能与蛇体重叠的bug

### Changed

- 缩小地图以加快游戏节奏
- 单人模式加快奖励生成的频率

## Version 1.2.1 - 2024-06-13-23:30

### Added

- 双人模式增加中立资源以提高对抗性

### Fixed

- 修复了快速掉头有延迟的bug

### Changed

- 修改部分颜色以提高视觉舒适程度
- 调整中立资源参数

## Version 1.2.2 2024-06-14-13:00

### Added

- 增加断尾功能

### Changed

- 将蛇体颜色改为渐变色以增强视觉体验

## Version 1.2.3 2024-06-14-19:00

### Fixed

- 修复了新食物可能覆盖旧食物或永久地形的bug

## Version 2.1.1 2024-10-03-02:47

为了提高单人游玩的游戏体验，并考虑到双手同时操作对部分人来说难度过大，本版本推出全新的**Solo**模式，使得玩家可以单手进行游戏，同时增加了人机交互。

### Added

- 增加了**Survival**的**Solo**模式

### Fixed

- 修复了潜在的新食物可能覆盖旧食物的bug

### Changed

- 对游戏模式进行了重新命名
- **Battle**模式为原来的双人模式，**Survival**的**Pair**模式为原来的单人模式
