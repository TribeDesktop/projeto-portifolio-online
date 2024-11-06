import styles from './Login.module.css'; // Atualizado para usar CSS Modules
import { Link } from 'react-router-dom';
import useAuthStore from '../../../store/useAuthStore';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import general from '../../../assets/images/general/general';
import logos from '../../../assets/images/logos/logos';
import icons from '../../../assets/images/icons/icons';

const schema = z.object({
  email: z.string().email('Invalid Email').min(1, 'Email is required'),
  password: z.string().min(6, 'Password must be at least 6 characters long'),
});

const Login = () => {
  const login = useAuthStore((state) => state.login);
  const error = useAuthStore((state) => state.error);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = (data) => {
    login(data.email, data.password);
  };

  return (
    <div className={styles.loginContainer}>
      <div className={styles.loginLeft}>
        <img src={logos.blueHalf.src} alt={logos.blueHalf.alt} id={styles.miniLogo} />
        <div className={styles.loginLeftTitle}>
          <h1>Portal do Aluno</h1>
          <p>Faça o login para acessar a sua conta</p>
        </div>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className={styles.inputGroup}>
            {errors.email && errors.password && (
              <p style={{ color: 'red', whiteSpace: 'nowrap' }}>Email ou senha incorreto. Tente novamente!</p>
            )}
            <img
              src={errors.email ? icons.emailRed.src : icons.email.src}
              alt={icons.email.alt}
              className={styles.imgInputs}
            />
            <input
              type="text"
              {...register('email')}
              className={errors.email ? styles.inputError : styles.inputFormStudent}
              placeholder="E-mail Institucional"
              required
            />
          </div>
          <div className={styles.inputGroup}>
            <img src={errors.password ? icons.lockRed.src : icons.lock.src} className={styles.imgInputs} />
            <input
              type="password"
              {...register('password')}
              className={errors.password ? styles.inputError : styles.inputFormStudent}
              placeholder="Senha"
              required
            />
          </div>

          <button type="submit" className={styles.loginButtonStudent}>
            Entrar
          </button>

          {error && <p style={{ color: 'red' }}>{error}</p>}
          <div className={styles.loginLeftBottom}>
            <Link className={styles.forgotLinkStudent} to={'/professor/teacherLogin'}>
              Sou funcionário
            </Link>
          </div>
        </form>
      </div>
      <div className={styles.loginRight}>
        <div className={styles.loginLogo}>
          <img src={logos.white.src} alt={logos.white.alt} />
        </div>
        <img src={general.banner.src} alt={general.banner.alt} className={styles.loginImage} />
      </div>
    </div>
  );
};

export default Login;
