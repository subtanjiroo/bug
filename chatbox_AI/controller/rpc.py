# import xmlrpc.client

# url = 'http://localhost:8069'
# username = 'agencycanhcam@gmail.com'
# password = 'odoo'
# db = 'CanhcamAgency'

# common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
# print(common.version())

# user_uid = common.authenticate(db, username, password, {})
# print(user_uid)

# 'xmlrpc/2/object' 'execute_kw'
# 'db, uid, password, model_name, method_name, [], {}'

# models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
# #search ids
# property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search', [[]])
# print("ids: ",property_ids)

# #count ids
# count_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_count', [[]])
# print("count: ",count_property_ids)

# #read ids
# read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'read', [property_ids],{'fields': ['name']})
# print("read: ",read_property_ids)

# #search and read ids
# search_read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_read', [[]],{'fields': ['name']})
# print("search and read: ",search_read_property_ids)

# # # create function
# # create_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'create', [{"name":'Property From RPC','sales_id':6}])
# # print("create: ",create_property_ids)

# # #write function
# # write_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'write', [[9], {"name":'Property update From RPC'}])
# # read_name_get = models.execute_kw(db, user_uid, password, 'estate.property', 'name_get', [[9]])
# # print("updated:  ",read_name_get)

# # #unlink
# # unlink_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'unlink', [[11]])
# # print("unlink:  ",unlink_property_ids)