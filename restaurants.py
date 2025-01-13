def most_varied_visitor(visits):

    hash_table = {}

    for visitors in visits.values():
        unique_visitors = set(visitors)

        for curr_visitor in unique_visitors:
            if curr_visitor not in hash_table:
                hash_table[curr_visitor] = 1
            else:
                hash_table[curr_visitor] += 1

    best_visitor = None
    best_count = None
        
    for visitor, count in hash_table.items():
        if best_count is None or count > best_count:
            best_visitor = visitor
            best_count = count

    return best_visitor

visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")