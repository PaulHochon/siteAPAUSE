require 'test_helper'

class AquaponieControllerTest < ActionController::TestCase
  test "should get index" do
    get :index
    assert_response :success
  end

end
