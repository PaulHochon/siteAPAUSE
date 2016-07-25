class CreateMeteoMesures < ActiveRecord::Migration
  def change
    create_table :meteo_mesures do |t|
      t.integer :lumiere, null: false, precision: 4
      t.decimal :temperature, null: false, precision: 3, scale: 1
      t.decimal :pression, null: false, precision: 6, scale: 2
      t.integer :humidite, null: false, precision: 2
      t.integer :pluie, null: false, precision: 1
    end
  end
end
