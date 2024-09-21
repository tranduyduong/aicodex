'use strict';

/**
 * Checks if the input is a string of 4 or more incremental digits.
 *
 * @param {string} input - The input string to be checked.
 * @returns {boolean} - Returns true if the input is a string of 4 or more incremental digits, otherwise false.
 */
function isIncremental(input) {
  // Check if input is a string of 4 or more digits
  if (!/^\d{4,}$/.test(input)) {
    return false;
  }

  // Convert the string to an array of digits
  const digits = Array.from(input, Number);

  // Check if the digits are incremental
  for (let i = 1; i < digits.length; i++) {
    if (digits[i] !== digits[i - 1] + 1) {
      return false;
    }
  }

  return true;
}

exports.isIncremental = isIncremental;

exports.calculate = function(req, res) {
  req.app.use(function(err, _req, res, next) {
    if (res.headersSent) {
      return next(err);
    }

    res.status(400);
    res.json({ error: err.message });
  });

  if (!req.query.operation) {
    throw new Error("Unspecified operation");
  }

  var operation = operations[req.query.operation];
  if (!operation) {
    throw new Error("Invalid operation: " + req.query.operation);
  }

  if (!req.query.operand1 ||
      !req.query.operand1.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      req.query.operand1.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid operand1: " + req.query.operand1);
  }

  if (!req.query.operand2 ||
      !req.query.operand2.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      req.query.operand2.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid operand2: " + req.query.operand2);
  }

  res.json({ result: operation(req.query.operand1, req.query.operand2) });
};

