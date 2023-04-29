from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'oatmeal': {
        'вода, л': 0.5,
        'овсянные хлопья, ст.ложек': 4.5
    }
}

def recipe_view(request, recipe: str):
    servings = int(request.GET.get('servings', 1))
    template_name = 'index.html'
    context = {}
    new_recipe = {}
    for dish, recipe_ in DATA.items():
        if dish == recipe:
            for ingredient, amount in recipe_.items():
                new_amount = amount * servings
                new_recipe[ingredient] = new_amount
            context['recipe'] = new_recipe
    return render(request, template_name, context)
