# Name, adjective, noun
mad_libs = "{} laughed at the {} {}."
print( mad_libs.format("Bobby", 'alien', 'Green'))
print( mad_libs.format('Tamato', 'potato', 'carrot' ))

print()

mad_libs = "{2} laughed at the {1} {0}."
print( mad_libs.format("Rajath", 'silly', 'alien'))
print( mad_libs.format('Tamato', 'potato', 'carrot' ))

print()

mad_libs = "{name} laughed at the {adjective} {noun}."
print( mad_libs.format(name = "Rajath", adjective = 'silly', noun = 'alien'))
print( mad_libs.format(name = 'Tamato', adjective = 'potato',noun =  'carrot' ))

print( mad_libs.format(adjective = 'potato',name = 'Tamato',noun =  'carrot' ))

