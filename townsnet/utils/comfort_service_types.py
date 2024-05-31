COMFORT_SERVICE_TYPES = {
  'education': [
    {
      'name': 'art_school',
      'name_ru': 'школа искусств',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 8,
      'osm_tags': {
        'amenity': 'music_school'
      }
    },
  ],
  'healthcare': [
    {
      'name': 'city_hospital',
      'name_ru': 'городская больница (д/в)',
      'weight': 0.5,
      'accessibility': 60,
      'demand': 9,
      'osm_tags': {
        'amenity': 'hospital'
      }
    },
    {
      'name': 'commercial_clinic',
      'name_ru': 'коммерческая клиника',
      'weight': 0.3,
      'accessibility': 60,
      'demand': 9,
      'osm_tags': {
        'amenity': 'clinic'
      }
    },
  ],
  'commerce': [
    {
      'name': 'hypermarket',
      'name_ru': 'ТРК / гипермаркет',
      'weight': 0.5,
      'accessibility': 30,
      'demand': 10,
      'osm_tags': {
        'shop': 'mall'
      }
    },
    {
      'name': 'specialized_store',
      'name_ru': 'профильный магазин',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 10,
      'osm_tags': {
        'shop': '*'
      }
    },
  ],
  'catering': [
    {
      'name': 'food_court',
      'name_ru': 'фудкорт',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 105,
      'osm_tags': {
        'amenity': 'food_court'
      }
    },
  ],
  'leisure': [
    {
      'name': 'library',
      'name_ru': 'медиатека / библиотека',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 100,
      'osm_tags': {
        'amenity': 'library'
      }
    },
    {
      'name': 'cult_object',
      'name_ru': 'культовый объект',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 100,
      'osm_tags': {
        'building': 'church'
      }
    },
  ],
  'recreation': [
    {
      'name': 'amusement_park',
      'name_ru': 'парк развлечений',
      'weight': 0.2,
      'accessibility': 60,
      'demand': 100,
      'osm_tags': {
        'tourism': 'theme_park'
      }
    },
    {
      'name': 'dog_park',
      'name_ru': 'площадка для выгула собак',
      'weight': 0.2,
      'accessibility': 15,
      'demand': 53,
      'osm_tags': {
        'tourism': 'theme_park'
      }
    },
  ],
  'sport': [
    {
      'name': 'swimming_pool',
      'name_ru': 'ФОК / бассейн',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 8,
      'osm_tags': {
        'leisure': 'swimming_pool'
      }
    },
  ],
  'service': [
  
  ],
  'transport': [
    {
      'name': 'railway_station',
      'name_ru': 'ЖД станция',
      'weight': 0.3,
      'accessibility': 15,
      'demand': 50,
      'osm_tags': {
        'railway': 'station'
      }
    },
    {
      'name': 'car_service',
      'name_ru': 'автосалон / автосервис',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 50,
      'osm_tags': {
        'shop': 'car_repair'
      }
    },
  ],
  'safeness': [
    {
      'name': 'fire_station',
      'name_ru': 'пожарное депо',
      'weight': 0.5,
      'accessibility': 15,
      'demand': 20,
      'osm_tags': {
        'amenity': 'fire_station'
      }
    },
  ]
}