var isLogEnabled = true;

function init(pIsLogEnabled) {
  isLogEnabled = pIsLogEnabled;    
}

function log(msg) {
  if (isLogEnabled) {
    console.log(new Date().toLocaleString() + " " + msg);
  }
}

module.exports = {
  init: init,
  log: log,
};
