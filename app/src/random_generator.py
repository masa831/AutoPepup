import math
import random


class RandomGenerator:
    """RandomGenerator (class)

    乱数値生成クラス。

    Attributes
        __max_value (int or float): 乱数生成範囲の最大値。
        __min_value (int or float): 乱数生成範囲の最小値。
        __sampling_value (int or float): 生成乱数のサンプリング値。
    """

    def __init__(self, value_1, value_2, sampling_value):
        """ __init__ (method)

        random_generatorの初期化メソッド。
        value_1、value_2のうち大きい値を最大値、小さい値を最小値とする。

        Args:
            value_1 (int or float): 乱数生成範囲の最大値もしくは最小値。
            value_2 (int or float): 乱数生成範囲の最大値もしくは最小値。
            sampling_value (int or float): 生成乱数のサンプリング値。
        """
        self.__max_value = max(value_1, value_2)
        self.__min_value = min(value_1, value_2)
        self.__sampling_value = sampling_value

    def generate_rand_value(self):
        """generate_rand_value (method)

        予め指定された範囲とサンプリング値を利用して、乱数を生成するメソッド。

        Returns:
            int or float: 生成した乱数。
        """
        # 小数を整数に変換するため、一括管理
        datas = [self.__max_value, self.__min_value, self.__sampling_value]

        # 小数を整数に変換するためのスケール値算出
        scale = 1
        while True:
            # 小数が存在する値のみ残す
            datas = [(d*scale*10) for d in datas if ((d - math.floor(d)) != 0)]
            # 小数が存在しない場合はbreak
            if not datas:
                break
            # スケール値を10倍していく
            scale *= 10

        # 小数を整数に変換
        max_scale_value = int(scale*self.__max_value)
        min_scale_value = int(scale*self.__min_value)
        step_scale_value = int(scale*self.__sampling_value)

        # 乱数を取得
        scale_value = random.randrange(min_scale_value,
                                       max_scale_value,
                                       step_scale_value)
        # 取得した乱数のスケールを戻す
        generate_value = scale_value/scale

        # 整数の場合は、intでキャスト
        if scale == 1:
            generate_value = int(generate_value)

        return generate_value
