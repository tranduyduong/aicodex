require('./helpers');
const { isIncremental } = require('./controller');

describe('isIncremental Function', () => {
  it('returns true for a string of 4 incremental digits', () => {
    expect(isIncremental('1234')).toBe(true);
  });

  it('returns true for a string of more than 4 incremental digits', () => {
    expect(isIncremental('12345')).toBe(true);
  });

  it('returns false for a string of less than 4 digits', () => {
    expect(isIncremental('123')).toBe(false);
  });

  it('returns false for a string with non-incremental digits', () => {
    expect(isIncremental('1245')).toBe(false);
  });

  it('returns false for a string with non-digit characters', () => {
    expect(isIncremental('12a4')).toBe(false);
  });

  it('returns false for an empty string', () => {
    expect(isIncremental('')).toBe(false);
  });

  it('returns false for a string with negative digits', () => {
    expect(isIncremental('-1234')).toBe(false);
  });

  it('returns false for a string with spaces', () => {
    expect(isIncremental('1 234')).toBe(false);
  });
});