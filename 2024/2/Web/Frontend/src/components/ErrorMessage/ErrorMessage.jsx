import iconError from '../../assets/img/icon-error.png';

const ErrorMessage = () => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        gap: '10px',
      }}
    >
      <img src={iconError} alt="error icon"></img>
      <p style={{ color: 'red', whiteSpace: 'nowrap' }}>Email ou senha incorreto. Tente novamente!</p>
    </div>
  );
};

export default ErrorMessage;
