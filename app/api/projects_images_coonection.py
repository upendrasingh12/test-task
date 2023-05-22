from app.config.settings import settings
from fastapi.responses import JSONResponse
from app.utils.s3connection import connect_s3
from app.config.database import connect_database
from fastapi import APIRouter, HTTPException, Request
from pprint import pprint

#Api Router
router = APIRouter()

#S3 connection
s3_client = connect_s3()

#Database connection
connection = connect_database()


@router.get("/labels")
async def get_labels():
    connection = connect_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT m1.title AS category, m1.id AS category_id, m2.title AS brand_name, m2.brand_id AS brand_id, m3.title AS style_name, m3.id AS style_id FROM materials m1 LEFT JOIN materials m2 ON m2.parent_id = m1.id LEFT JOIN ( SELECT id, title, parent_id FROM materials ) m3 ON m3.parent_id = m2.id WHERE m1.parent_id = 0 ORDER BY category ASC;")
            fetch_labels = cursor.fetchall()
            labels = fetch_labels
            output = {}

            for item in labels:

                category_id = item['category_id']
                name = item['category']

                brand_id = item['brand_id']
                brand_name = item['brand_name']
                
                style_id = item['style_id']
                style_name = item['style_name']

                if category_id not in output:
                    output[category_id] = {'cat_id': category_id,'name': name, 'brands': {}}

                if brand_id not in output[category_id]['brands']:
                    output[category_id]['brands'][brand_id] = {'brand_id': brand_id,'brand_name': brand_name, 'styles': {}}

                if style_id not in output[category_id]['brands'][brand_id]['styles']:
                    output[category_id]['brands'][brand_id]['styles'][style_id] = {'style_id' : style_id, 'style_name' : style_name}

        # pprint(output)


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

    return JSONResponse(content=output)
