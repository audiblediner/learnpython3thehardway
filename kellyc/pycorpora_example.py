# # Python 2!!
# from pycorpora import plants, colors
# import random
#
# random_flowers = random.sample(plants.flowers["flowers"], 10)
# random_colors = random.sample(
#     [item['color'] for item in colors.crayola["colors"]], 10)
# for pair in zip(random_colors, random_flowers):
#     print (" ".join(pair).title())
#
# # outputs (e.g.):
# #   Maroon Bergamot
# #   Blue Bell Zinnia
# #   Pink Flamingo Camellias
# #   Tickle Me Pink Begonia
# #   Burnt Orange Clover
# #   Fuzzy Wuzzy Hibiscus
# #   Outer Space Forget Me Not
# #   Almond Petunia
# #   Pine Green Ladys Slipper
# #   Shadow Jasmine
#
# from pycorpora import animals, objects
# import random
# random_dinosaur = random.sample(animals.dinosaurs["dinosaurs"], 10)
# random_object = random.sample(objects.objects["objects"], 10)
# for pair in zip(random_dinosaur, random_object):
#     print(" ".join(pair).title())
#
# # outputs (e.g.):
# # Laplatasaurus Rhino
# # Jeholosaurus Sticky Note
# # Proterosuchid Quilt
# # Daptosaurus Spring
# # Geranosaurus Martini Glass
# # Lancanjiangosaurus Bow Tie
# # Panphagia Phone
# # Daemonosaurus Rolling Pin
# # Eodromaeus Spool Of Thread
# # Bicentenaria Hanger
#
#
# "After the [event] all we had to eat were cans of [food]. Then the [creatures] came. I wish we had never moved to [place]. It's like a bad episode of [tv_shows]."
#
from pycorpora import humans, archetypes, mythology, geography, foods, technology
import random

def a_tale():
    return "After the {0} all we had to eat were cans of {1}.  Then the {2} came. I wish we had never moved to {3}. I blame it on {4}.".format(
        random.choice(archetypes.event["events"])["name"],
        random.choice(foods.menuItems["menuItems"]),
        random.choice(mythology.lovecraft["deities"]),
        random.choice(geography.us_cities["cities"])["city"],
        random.choice(technology.new_technologies["technologies"])
        )

    # random.choice((archetypes.event["events"])["name"]),
    # random.choice(foods.menuItems["menuItems"]),
    # random.choice(mythology.lovecraft["lovecraft"]),
    # random.choice((geography.us_cities["cities"])["city"]),
    # random.choice(film-tv.tv_shows["tv_shows"])


for i in range(5):
    print a_tale()


# from pycorpora import humans, geography
# import random
#
# def a_biography():
#     return "{0} is a(n) {1} who lives in {2}.".format(
#         random.choice(humans.firstNames["firstNames"]),
#         random.choice(humans.occupations["occupations"]),
#         random.choice(geography.us_cities["cities"])["city"]
# )
#
# for i in range(5):
#     print a_biography()
