require('./helpers');
const { isIncremental } = require('./controller');

// black test suite
describe('isIncremental Function', () => {
  it('returns true for a string of 4 incremental digits', () => {
    expect(isIncremental('1234')).to.eql(true);
  });

  it('returns true for a string of more than 4 incremental digits', () => {
    expect(isIncremental('12345')).to.eql(true);
  });

  it('returns false for a string of less than 4 digits', () => {
    expect(isIncremental('123')).to.eql(false);
  });

  it('returns false for a string with non-incremental digits', () => {
    expect(isIncremental('1245')).to.eql(false);
  });

  it('returns false for a string with non-digit characters', () => {
    expect(isIncremental('12a4')).to.eql(false);
  });

  it('returns false for an empty string', () => {
    expect(isIncremental('')).to.eql(false);
  });

  it('returns false for a string with negative digits', () => {
    expect(isIncremental('-1234')).to.eql(false);
  });

  it('returns false for a string with spaces', () => {
    expect(isIncremental('1 234')).to.eql(true);
  });
});