test = {
  'name': 'q3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Remember that you should be using a list!;
          >>> type(event_result) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your list should have 5 elements.;
          >>> len(event_result) == 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Every element of your list should be a string.;
          >>> [type(i)== str for i in event_result] 
          [True, True, True, True, True]
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
