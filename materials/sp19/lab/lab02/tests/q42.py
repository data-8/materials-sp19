test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(above_eight) == tables.Table
          True
          >>> above_eight.num_rows == 20
          True
          >>> # Make sure your columns are in the right order!
          >>> # First column should be 'Title', second column should be 'Rating'
          >>> print(above_eight.sort(0).take([17]))
          Title       | Rating
          Toy Story 3 | 8.3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
