# import build_profile 
# usr=build_profile.build_profile('albert', 'einstein',location='princeton',field='physics')
# print(usr)

# from build_profile import build_profile as bp
# usr=bp('albert', 'einstein',location='princeton',field='physics')
# print(usr)


# import build_profile as bd
# usr=bd.build_profile('albert', 'einstein',location='princeton',field='physics')
# print(usr)


from build_profile import*
usr=build_profile('albert', 'einstein',location='princeton',field='physics')
print(usr)