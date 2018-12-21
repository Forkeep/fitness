from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'calorie_calculator/index.html')


def cal_calculator(request):
    print("调用了cal_calculator")
    weight = request.POST['weight']
    cal_per_wei = request.POST['cal_per_wei']
    protein = request.POST['protein']
    carbohydrate = request.POST['carbohydrate']
    fat = request.POST['fat']
    weight = float(weight)
    cal_per_wei = float(cal_per_wei)
    protein = float(protein)
    carbohydrate = float(carbohydrate)
    fat = float(fat)
    print(type(fat))

    print(fat)

    all_calorie = weight*cal_per_wei
    print(all_calorie)
    eat_protein = all_calorie*protein/4
    print(eat_protein)
    eat_carbohydrate = all_calorie*carbohydrate/4
    eat_fat = all_calorie*fat/9
    context = {'eat_protein':eat_protein,'eat_carbohydrate':eat_carbohydrate,'eat_fat':eat_fat}
    return render(request,'calorie_calculator/cal_calorie.html',context=context)


def power_calculator(request):
    barbell = request.POST['barbell']
    total_wei = request.POST['total_wei']
    # 输入目前是最大重量的百分之多少
    now_level = request.POST['now_level']
    max_power = total_wei/now_level
    max_power_95 = max_power*0.95
    max_power_90 = max_power*0.90
    max_power_80 = max_power*0.80
    max_power_70 = max_power*0.70
    max_power_60 = max_power*0.60
    context = {'max_power':max_power,'max_power_95':max_power_95,
               'max_power_90':max_power_90,'max_power_80':max_power_80,
               'max_power_70':max_power_70,'max_power_60':max_power_60}
    return render(request,'base.html',context=context)
