#Start with some designs that need to be printed.
import printing_functions as pt
unprinted_designs=['phone case','robot pendant','dodecachedron']
completed_models=[]

pt.print_models(unprinted_designs[:],completed_models)
pt.show_completed_models(completed_models)
#show_completed_models(completed_models)
print("\n")
pt.print_models(unprinted_designs,completed_models)
pt.show_completed_models(completed_models)



