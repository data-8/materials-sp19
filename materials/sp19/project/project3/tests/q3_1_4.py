test = {
  'name': 'q3_1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> genre_and_distances.take(np.arange(5)).group('Genre').index_by('Genre')[my_assigned_genre][0].item('count') >= 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_assigned_genre_was_correct == (my_assigned_genre == 'action')
          True
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
