def seed(cx):
    cx.execute("""
      INSERT INTO studios VALUES ('CENTER','青苔主校'),('EAST','东桥课点'),('WEST','槐树共创坊') ON CONFLICT DO NOTHING;
      INSERT INTO workshops VALUES ('CLASS-17','冬日手捏花盏','CENTER','2026-11-19','2026-12-01'),
        ('CLASS-18','山纹调色碟','EAST','2026-11-20','2026-12-03') ON CONFLICT DO NOTHING;
      INSERT INTO ceramics VALUES ('POT-11','CLASS-17','蓝釉花盏','CX-11','ready','CENTER'),
        ('POT-12','CLASS-17','方口红泥盏','CX-12','collected','CENTER'),
        ('POT-13','CLASS-17','白泥折边盏','CX-13','ready','WEST'),
        ('POT-21','CLASS-18','灰绿浅碟','CX-21','ready','EAST') ON CONFLICT DO NOTHING;
      INSERT INTO claim_checks VALUES ('POT-12','CENTER','2026-11-20','邱同学','operator@demo.local')
        ON CONFLICT DO NOTHING;
    """)
