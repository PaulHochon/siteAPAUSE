class MeteoController < ApplicationController
	def index
		@meteo_mesures=MeteoMesure.last #récupération de la dernière mesure entrée dans la BDD pour simuler le temps réel.
  										#Rappel : cette donnée est censée être mise à jour chaque minute.
	end
end
