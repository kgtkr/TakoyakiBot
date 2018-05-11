# coding: utf-8
import csv
import random
import os
from datetime import datetime


class Takoyaki:

    def __init__(self, tweet_type):

        # tweet_type = 0: 通常の定期ツイ, 1: テスト, 2: リプ
        self.tweet_type = tweet_type

        self.toppings = []
        self.ingredients = []

        self.takoyaki_num = self.ingredients_num = 0
        self.choose_ingredients = self.choose_topping = []

        self.price = self.calories = 0

        # 買えなかった理由
        self.reasons = ["お金が足りませんでした。", "ダイエット中なのでたこ焼きを控えることにしました。",
                        "買い忘れてしまいました。", "寿司に浮気してしまいました。"]

        # たこ焼きを買う個数
        self.takoyaki_set = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59]

        # 時刻ごとのメッセージ
        self.time_data = {4: ["早朝", "早く寝ましょう。"],
                          8: ["モーニング", "おはようございます。"],
                          12: ["ランチ", "眠くならない程度に食べましょう。"],
                          16: ["遅めのおやつ", "おやつだおやつだー"],
                          20: ["ディナー", "1日お疲れ様でした。"],
                          0: ["深夜", "たこ焼きは美味しいので深夜に食べても大丈夫です。"]}

        # リプのメッセージ
        self.reply_data = ["もちもち", "もこもこ", "もふもふ", "すくすく", "なふなふ", "にゃーにゃー",
                           "たこたこ", "にゅるる", "にゃふっ", "もっちもっち", "もっちぃぃぃ", "はいプロ",
                           "もっこもこ", "みゃー", "がおー", "たこたこたこたこ", "ゴリー"]


    def information_load(self):

        with open("./Data/toppings.csv", "r") as f:
            data = csv.reader(f)
            for line in data:
                self.toppings.append(line)

        with open("./Data/ingredients.csv", "r") as f:
            data = csv.reader(f)
            for line in data:
                self.ingredients.append(line)


    def choose_order(self):

        # たこ焼きを買う個数
        self.takoyaki_num = random.choice(self.takoyaki_set)
        # 具の種類数。1~3個
        self.ingredients_num = random.randrange(3) + 1

        self.choose_ingredients = random.sample(self.ingredients, self.ingredients_num)
        self.choose_topping = random.choice(self.toppings)


    def calculate(self):

        # 値段とカロリーの計算
        # 15円と30キロカロリーはたこ焼きのタネの分
        self.price, self.calories = 15, 30

        for i in range(self.ingredients_num):
            self.price += int(self.choose_ingredients[i][1])
            self.calories += int(self.choose_ingredients[i][2])

        self.price += int(self.choose_topping[1])
        self.calories += int(self.choose_topping[2])

        self.price *= self.takoyaki_num
        self.calories *= self.takoyaki_num


    def make_tweet(self):

        # ツイートの作成
        if self.tweet_type == 0:
            now_time =int((datetime.utcnow().hour + 9) % 24)
            res = self.time_data[now_time][0] + "のたこ焼きです。\n\n"
        elif self.tweet_type == 1:
            res = "テスト\n\n"
        else:
            res = "ご注文ありがとうございますたこ。"

        res += str(self.takoyaki_num) + "個注文しました。\n\n"
        res += "具材: "

        for i in range(self.ingredients_num):
            res += self.choose_ingredients[i][0]
            if i == self.ingredients_num - 1:
                res += "\n"
            else:
                res += " "

        res += "味  : " + self.choose_topping[0] + "\n\n"
        res += str(self.price) + "円でした。\n"
        res += "合計" + str(self.calories) + "キロカロリーです\n\n"

        if self.tweet_type == 0:
            res += self.time_data[now_time][1]
        elif self.tweet_type == 1:
            res += "テスト成功"
        else:
            res += rancom.choice(self.reply_data) + "\n"
            res += "またのお越しをお待ちしておりますたこ。"

        return res 


    def nyan(self):

        self.information_load()

        self.choose_order()

        # たこ焼きを買わなかった
        if self.takoyaki_num == 0:
            return random.choice(self.reasons)

        self.calculate()

        tweet = self.make_tweet()

        return tweet
