#include "dicelib.hpp"
#include <algorithm>
#include <array>
#include <random>

namespace dicelib
{
    std::vector<int> roll(int n)
    {
        if (n <= 0)
            return {};

        std::mt19937 rng{std::random_device{}()};
        std::uniform_int_distribution<int> dist(1, 6);

        std::vector<int> res(n);
        for (int &el : res)
        {
            el = dist(rng);
        }

        return res;
    }

    Figure get_figure(const std::vector<int> &dices)
    {
        Figure res{Figure::NOTHING};

        if (dices.size() == 5)
        {
            std::array<int, 7> freq{};
            for (int d_val : dices)
            {
                if (d_val >= 1 && d_val <= 6)
                {
                    freq[d_val]++;
                }
            }

            int max_freq = *std::max_element(freq.begin() + 1, freq.end());
            if (max_freq == 5)
            {
                res = Figure::POKER;
            }
            else if (max_freq == 4)
            {
                res = Figure::FOUR_OF_KIND;
            }
            else
            {
                bool triplet{max_freq == 3};
                int pairs_count = [&](int val)
                {
                    int counter = 0;
                    for (std::size_t i = 1; i <= 6; ++i)
                    {
                        if (freq[i] >= val)
                        {
                            ++counter;
                        }
                    }
                    return counter;
                }(2);

                if (triplet && pairs_count >= 2)
                {
                    res = Figure::FULL_HOUSE;
                }
                else if (freq[2] && freq[3] && freq[4] && freq[5] && freq[6])
                {
                    res = Figure::LARGE_STRAIGHT;
                }
                else if (freq[1] && freq[2] && freq[3] && freq[4] && freq[5])
                {
                    res = Figure::SMALL_STRAIGHT;
                }
                else if (triplet)
                {
                    res = Figure::THREE_OF_KIND;
                }
                else if (pairs_count)
                {
                    res = pairs_count > 1 ? Figure::TWO_PAIRS : Figure::ONE_PAIR;
                }
            }
        }

        return res;
    }

    Result compare(const std::vector<int> &p1, const std::vector<int> &p2)
    {
        int res1 = static_cast<int>(get_figure(p1));
        int res2 = static_cast<int>(get_figure(p2));
        if (res1 > res2)
        {
            return Result::P1_WINS;
        }
        else if (res2 > res1)
        {
            return Result::P2_WINS;
        }

        return Result::DRAW;
    }
}