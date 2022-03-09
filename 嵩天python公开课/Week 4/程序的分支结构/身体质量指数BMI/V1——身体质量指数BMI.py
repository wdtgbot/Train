def main():
    height, weight = eval(input("请输入身高（米）和体重（公斤）【逗号隔开】："))
    bmi = weight / pow(height, 2)
    print("BMI指数为：{:.2f}".format(bmi))
    if bmi < 18.5:
        who = "偏廋"
    elif 18.5 <= bmi < 25:
        who = "正常"
    elif 25 <= bmi < 30:
        who = "偏胖"
    else:
        who = "肥胖"
    print("BMI 指标为：国际'{0}'".format(who))


if __name__ == "__main__":
    main()
