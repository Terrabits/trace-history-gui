# Work Items

Outstanding work items.

## Use Settings string instead of font icon (for now)

Improve this if time permits

## Measurement Complete Dialog

Need to implement this.

## Move Timeout to Settings

This connection detail should not have main focus.

## Measure in Separate Thread

Do not lock up gui. Provide way to cancel measurement (turn start button into 'Stop').

## [<Ch>_]settings.csv

```python
header = [
  'if_bandwidth_Hz',
  'power_dBm',
  'points',
  'agc_mode',
  'swept_mode',
]
```

## Frequency data, header

Save frequency data in file `[<Ch>_]frequency_Hz.csv` with the following header:

```python
header_at = lambda index: f'point {index} Hz'
indexes   = range(1, points + 1)
header    = map(header_at, indexes)
```

## Trace Data, header

Save trace data in file `[<Ch>_]<Trace>.csv` with the following header:

```python
point_at  = lambda index: f'point {index // 2}'
re_im_at  = lambda index: 'real' if index % 2 else 'imag'
header_at = lambda index: f'{point_at(index)} {re_im_at(index)}'
indexes   = range(1, 2 * points + 1)
header    = map(header_at, indexes)
```
