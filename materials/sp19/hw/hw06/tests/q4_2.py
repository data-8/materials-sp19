test = {
  'name': 'q4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> representative_sample.num_rows == 500
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(np.in1d(representative_sample.column('mag'), earthquakes.column('mag')))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> representative_mean < max(representative_sample.column('mag')) and representative_mean > min(representative_sample.column('mag')) 
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
