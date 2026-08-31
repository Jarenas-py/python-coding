from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

productList = []

class Product(BaseModel):
    name: str
    price: float
    description: str

@app.get("/")
def root():
    return {"Hello" : "World"}

@app.post("/product")
def createItem(product: Product):
    productList.append(product)
    return {"Product Added" : product.name}

@app.get("/product")
def allProducts():
    return productList

@app.get("/product/{product_id}")
def exactProduct(product_id : int):
    return {f"Product {product_id}" : productList[product_id]}

@app.put("/product/{product_id}")
def updateProduct(product_id : int, product : Product):
    productList[product_id] = product
    return {"Product Updated" : product.name}

@app.delete("/product/{product_id}")
def deleteProduct(product_id : int):
    del productList[product_id]
    print("Product {product_id} has been succesfully deleted!")
    return productList