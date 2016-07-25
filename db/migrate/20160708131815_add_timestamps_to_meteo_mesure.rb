class AddTimestampsToMeteoMesure < ActiveRecord::Migration
  def change
    add_column :meteo_mesures, :created_at, :datetime
    add_column :meteo_mesures, :updated_at, :datetime
  end
end
