import styles from './TeacherLogin.module.css';
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

const TeacherLogin = () => {
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
          <h1>Portal do Professor</h1>
          <p>Faça o login para acessar a sua conta</p>
        </div>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className={styles.inputGroup}>
            {errors.email && errors.password && (
              <p style={{ color: 'red', whiteSpace: 'nowrap' }}>Email ou senha incorreto. Tente novamente!</p>
            )}
            <img src={icons.email.src} className={styles.icon} alt={icons.email.alt} />
            <input
              type="text"
              {...register('email')}
              className={styles.inputTeacher}
              placeholder="E-mail Institucional"
              required
            />
          </div>
          <div className={styles.inputGroup}>
            <img src={icons.lock.src} alt={icons.lock.alt} />
            <input
              type="password"
              {...register('password')}
              className={styles.inputTeacher}
              placeholder="Senha"
              required
            />
          </div>

          <div className={styles.inputGroup}>
            <img src={icons.hat.src} alt={icons.hat.alt} />
            <select className={styles.selectContainer}>
              <option value="Instituição de Ensino">Instituição de Ensino</option>
              <option value="FATEC Americana">FATEC Americana</option>
              <option value="FATEC Araçatuba">FATEC Araçatuba</option>
              <option value="FATEC Araraquara">FATEC Araraquara</option>
              <option value="FATEC Barueri">FATEC Barueri</option>
              <option value="FATEC Bauru">FATEC Bauru</option>
              <option value="FATEC Botucatu">FATEC Botucatu</option>
              <option value="FATEC Carapicuíba">FATEC Carapicuíba</option>
              <option value="FATEC Diadema">FATEC Diadema</option>
              <option value="FATEC Franca">FATEC Franca</option>
              <option value="FATEC Garça">FATEC Garça</option>
              <option value="FATEC Guaratinguetá">FATEC Guaratinguetá</option>
              <option value="FATEC Registro">FATEC Registro</option>
              <option value="FATEC Ribeirão Preto">FATEC Ribeirão Preto</option>
              <option value="FATEC São Bernardo do Campo">FATEC São Bernardo do Campo</option>
              <option value="FATEC São Paulo">FATEC São Paulo</option>
            </select>
          </div>

          <button type="submit" className={styles.loginButton}>
            Entrar
          </button>

          {error && <p style={{ color: 'red' }}>{error}</p>}
          <div className={styles.loginLeftBottom}>
            <Link className={styles.forgotLink} to={'/'}>
              Sou Aluno
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

export default TeacherLogin;
