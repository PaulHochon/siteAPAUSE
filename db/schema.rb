# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20160718100252) do

  create_table "aquaponie_mesures", force: :cascade do |t|
    t.integer  "circulation", limit: 4,                         null: false
    t.decimal  "pH",                    precision: 4, scale: 2, null: false
    t.decimal  "niveau",                precision: 3, scale: 1, null: false
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "meteo_mesures", force: :cascade do |t|
    t.integer  "lumiere",     limit: 4,                         null: false
    t.decimal  "temperature",           precision: 3, scale: 1, null: false
    t.decimal  "pression",              precision: 6, scale: 2, null: false
    t.integer  "humidite",    limit: 4,                         null: false
    t.integer  "pluie",       limit: 4,                         null: false
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end
