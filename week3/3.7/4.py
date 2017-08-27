from xml.etree import ElementTree


def calc_color_value(results, root, value):
    results[root.attrib["color"]] = results[root.attrib["color"]] + value
    for child in root:
        calc_color_value(results, child, value + 1)


results = {"red": 0, "blue": 0, "green": 0}
tree = ElementTree.fromstring(input().strip())
calc_color_value(results, tree, 1)
print(results["red"], results["green"], results["blue"])
