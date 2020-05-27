from pant import Pants

def check_results():
    pant = Pants('red', 35, 36, 15.12)
    assert pant.color == 'red'
    assert pant.waist_size == 35
    assert pant.length == 36
    assert pant.price == 15.12
    
    pant.change_price(10) == 10
    assert pant.price == 10 
    
    assert pant.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

    check_results()