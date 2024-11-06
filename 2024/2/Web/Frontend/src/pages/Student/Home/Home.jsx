import Menu from '../../../components/Student/Menu/Menu';
import Panel from '../../../components/Panel/Panel';
import icons from '../../../assets/images/icons/icons';
import styles from './Home.module.css';

const Home = () => {
  return (
    <div className={styles.homeContainer}>
      <Menu studentName={'Ana Clara'} />
      <div className={styles.homeSideContents}>
        <Panel pageName="Painel do Aluno" section="Início" color="#F66B0E" />
        <div className={styles.homeInfo}>
          <div className={styles.homeInfoTop}>
            <div className={styles.homeProfileStudent}>
              <div className={styles.cardTitle}>
                <img src={icons.user.src} alt={icons.user.alt} />
                <p>Perfil do aluno</p>
              </div>
              <div>
                <div className={styles.studentInfo}>
                  <p>Ana Clara</p>
                  <p>4º sem</p>
                </div>
                <p>000000000000000</p>
                <p>123456789</p>
              </div>
              <div>
                <p>Média Geral: 8.79</p>
              </div>
            </div>
            <div className={styles.homeCalendar}>
              <div className={styles.cardTitle}>
                <img src={icons.calendar.src} alt={icons.calendar.alt} />
                <p>Calendário</p>
                <img src={icons.arrowRight.src} alt={icons.arrowRight.alt} />
              </div>
              <div>
                <p>30/09/2024</p>
                <p>Reunião importante</p>
              </div>
              <div>
                <p>27/10/2024</p>
                <p>Provas</p>
              </div>
              <div className={styles.viewAll}>
                <p>ver tudo</p>
              </div>
            </div>
          </div>
          <div className={styles.homeInfoBelow}>
            <div className={styles.homeSection}>
              <div className={styles.cardTitle}>
                <img src={icons.calendar.src} alt={icons.calendar.alt} />
                <p>Visão Geral</p>
                <img src={icons.arrowRight.src} alt={icons.arrowRight.alt} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
