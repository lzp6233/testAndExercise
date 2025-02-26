# testAndExercise

## 游戏

### 贪吃蛇

+ 如何运行
    + 安装pygame
    ```bash
    pip install pygame
    ```
    + 运行
    ```bash
    python main.py
    ```

+ 游戏规则
    + 懂得都懂

2048游戏的规则如下：

1. **游戏目标**：通过合并相同的数字方块，尽可能地达到2048这个数字。

2. **游戏板**：游戏在一个4x4的方格板上进行。

3. **初始状态**：游戏开始时，板上会随机出现两个数字，通常是2或4。

4. **移动方块**：
   - 玩家可以使用上下左右方向键（在这个实现中是W、A、S、D键）来移动所有的方块。
   - 每次移动时，所有方块会尽可能地向指定方向滑动。
   - 如果两个相邻的方块数字相同，它们会合并成一个方块，其数字为原来两个方块数字之和。

5. **新方块生成**：每次玩家移动后，会在一个随机的空白位置生成一个新的方块，数字为2或4。

6. **游戏结束**：
   - 游戏在玩家无法进行任何有效移动时结束，即没有空格且没有相邻的相同数字可以合并。
   - 游戏结束时，玩家的得分是所有方块上数字的总和。

7. **胜利条件**：当一个方块的数字达到2048时，玩家获胜。不过，玩家可以选择继续游戏以获得更高的分数。

希望这些规则能帮助你更好地理解和享受2048游戏！如果有其他问题或需要进一步的帮助，请告诉我。
