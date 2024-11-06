import styles from './RollCall.module.css';
import Menu from '../../../components/Professor/TeacherMenu/TeacherMenu';
import Panel from '../../../components/Panel/Panel';
import icons from '../../../assets/images/icons/icons';

const RollCall = () => {
  return (
    <div className={styles.rollcallContainer}>
      <Menu studentName={'Sandra'} />
      <div className={styles.rollcallSideContents}>
        <Panel pageName="Portal do Professor" section="Início/Alunos/Presença" color="#F66B0E" />
        <h3 className={styles.unitIdentify}>Unidade de Ensino: Nome da Instituição</h3>
        <div className={styles.rollcallInfo}>
          <div className={styles.rollcallInfoTop}>
            <div className={styles.filters}>
              <label>Turma</label>
              <select className={styles.classSelect}>
                <option value="Selecione a Turma">Turma 1</option>
              </select>
              <label>Disciplina</label>
              <select className={styles.classSelect}>
                <option value="Selecione a Disciplina">Programação Web</option>
              </select>
            </div>
            <div className={styles.searchBar}>
              <input type="search" placeholder="Pesquisar aluno" />
            </div>
          </div>
          <table className={styles.attendanceTable}>
            <thead>
              <tr>
                <th>Nome</th>
                <th>1º</th>
                <th>2º</th>
                <th>3º</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className={styles.studentInfo}>
                  <img src={icons.user.src} alt={icons.user.alt} className={styles.avatar} />
                  <span>Nome Completo 1</span>
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
              </tr>
              <tr>
                <td className={styles.studentInfo}>
                  <img src={icons.user.src} alt={icons.user.alt} className={styles.avatar} />
                  <span>Nome Completo 2</span>
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
              </tr>
              <tr>
                <td className={styles.studentInfo}>
                  <img src={icons.user.src} alt={icons.user.alt} className={styles.avatar} />
                  <span>Nome Completo 3</span>
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
              </tr>
              <tr>
                <td className={styles.studentInfo}>
                  <img src={icons.user.src} alt={icons.user.alt} className={styles.avatar} />
                  <span>Nome Completo 4</span>
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
              </tr>
              <tr>
                <td className={styles.studentInfo}>
                  <img src={icons.user.src} alt={icons.user.alt} className={styles.avatar} />
                  <span>Nome Completo 5</span>
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
              </tr>
              <tr>
                <td className={styles.studentInfo}>
                  <img src={icons.user.src} alt={icons.user.alt} className={styles.avatar} />
                  <span>Nome Completo 6</span>
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
                <td>
                  <input type="checkbox" />
                </td>
              </tr>
            </tbody>
          </table>
          <button className={styles.updateButton}>Atualizar</button>
        </div>
      </div>
    </div>
  );
};

export default RollCall;
