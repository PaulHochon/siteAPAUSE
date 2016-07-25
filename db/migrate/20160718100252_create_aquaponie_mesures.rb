class CreateAquaponieMesures < ActiveRecord::Migration
  def change
    create_table :aquaponie_mesures do |t|
      t.integer :circulation, null: false, precision: 4
      t.decimal :pH, null: false, precision: 4, scale: 2
      t.decimal :niveau, null: false, precision: 3, scale: 1

      t.timestamps null: true
    end
  end
end
