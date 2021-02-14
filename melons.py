import random, datetime


"""Classes for melon orders."""

class AbstractMelonOrder():
    """Abstract class for melon orders."""

    def __init__(self, species, qty):

        self.species = species.lower()
        self.qty = qty
        self.shipped = False
       # except TooManyMelonsError 

        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")

    def get_total(self):
        """Calculate price, including tax."""
        
        def get_base_price():
            base_price = random.choice(range(5, 10))
            current_time = datetime.datetime.now().time()
            if datetime.time(hour=0) < current_time < datetime.time(hour=4):
                base_price += 4 
                
            return base_price
        
        base_price = get_base_price()

        if self.species == 'christmas melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10:
            total += 3
            
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


        

########

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08



#######################


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



######

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        """Takes a boolean input and updates whether or not the melon has passed inspection."""

        if passed == True:
            self.passed_inspection = True
        elif passed == False:
            self.passed_inspection = False


class TooManyMelonsError(ValueError):
    """Exception raised when creating order with more than 100 melons"""



