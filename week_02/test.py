@pytest.fixture
def global_list():
    #this is a fixture
    #can do prints or connect to db


    return [1, 2, 3]


# by adding the fixture as a decoration, this allows us to 
# pass the function as local variable which actually runs the 
# function and passes it's return.
def test_reverse_vanilla(global_list):
    # Set-up

    expected = [3, 2, 1]
    # The test
    reverse_list(global_list)

    #  Verify Results
    assert L == expected
    
    pass