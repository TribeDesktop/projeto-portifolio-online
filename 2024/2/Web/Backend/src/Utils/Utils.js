const handleError = (res, error, status = 500) => {
  res.status(status).json({ error: error.message || 'Erro no servidor' });
};

const response = (res, msg, status = 200) => {
  res.status(status).json(msg);
};

export { handleError, response };
