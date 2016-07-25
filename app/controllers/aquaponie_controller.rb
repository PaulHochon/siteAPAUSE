class AquaponieController < ApplicationController
  def index
  	@aquaponie_mesures=AquaponieMesure.last
  end
end
