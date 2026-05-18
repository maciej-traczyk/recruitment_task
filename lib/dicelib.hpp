#pragma once
#include <vector>

namespace dicelib
{
    enum class Figure : int
    {
        NOTHING = 0,
        ONE_PAIR = 1,
        TWO_PAIRS = 2,
        THREE_OF_KIND = 3,
        SMALL_STRAIGHT = 4,
        LARGE_STRAIGHT = 5,
        FULL_HOUSE = 6,
        FOUR_OF_KIND = 7,
        POKER = 8
    };

    enum class Result : int
    {
        DRAW = 0,
        P1_WINS = 1,
        P2_WINS = 2
    };

    std::vector<int> roll(int n);
    Figure get_figure(const std::vector<int> &dices);
    Result compare(const std::vector<int> &p1, const std::vector<int> &p2);
}
