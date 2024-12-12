from main_app.models import Product, Profile

class Cart():
    def __init__(self,request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=request.user.id)
            carty=str(self.cart)
            carty = carty.replace("\'", "\"")
            current_user.update(old_cart=str(carty))

            
            
            


            self.session['session_key'] = self.cart
            self.session.modified = True

    def db_add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
       

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True


    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
       

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_qaunts(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourcart= self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        thiing = self.cart
        return thiing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
    
    def cart_total(self):
        products_ids= self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)  
        quantity = self.cart
        total = 0
        for key, value in quantity.items():
            for product in products:
                if product.id == int(key):
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total
      
      
        