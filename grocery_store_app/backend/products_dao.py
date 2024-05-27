from sqlconnection import  get_sql_connection

def get_all_products(connection): 
    cursor=connection.cursor()
    query="SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id "
    cursor.execute(query)
    response=[] 
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
    return response

def insert_new_product(connection, product):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
        cursor.execute(query, (product['product_name'], product['uom_id'], product['price_per_unit']))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        raise e
    finally:
        cursor.close()

def delete_product(connection,product_id):
    cursor= connection.cursor()
    query=("DELETE FROM products where product_id=" +str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__=='__main__':
    connection= get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))