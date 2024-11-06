import useAuthStore from '../../../store/useAuthStore.js';
import styles from './Students.module.css';

const Students = () => {
  const { students } = useAuthStore();

  return (
    <div className={styles.studentsContainer}>
      <aside className={styles.sidebar}>
        <div className={styles.profile}>
          <img src="user_image_url" alt="Profile" />
          <p>Nome dado:</p>
        </div>
        <nav className={styles.menu}>
          <ul>
            <li>Alunos</li>
            <li>Notas</li>
            <li>Planejamento</li>
            <li>Conteúdos</li>
            <li>Calendário</li>
          </ul>
        </nav>
        <div className={styles.settings}>
          <p>Configurações</p>
          <p>Sair</p>
        </div>
      </aside>

      <main className={styles.mainContent}>
        <header className={styles.header}>
          <h1>Portal do Professor</h1>
          <div className={styles.filters}>
            <div>
              <label>Turma:</label>
              <select>
                <option>Selecione uma Turma</option>
              </select>
            </div>
            <div>
              <label>Disciplina:</label>
              <select>
                <option>Selecione uma Disciplina</option>
              </select>
            </div>
          </div>
          <div className={styles.actions}>
            <input type="text" placeholder="Pesquisar aluno" />
            <button>Chamada</button>
          </div>
        </header>

        <section className={styles.studentList}>
          <table>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Situação</th>
                <th>Frequência</th>
              </tr>
            </thead>
            <tbody>
              {students.map((student) => (
                <tr key={student.id}>
                  <td>{student.name}</td>
                  <td>{student.status}</td>
                  <td>
                    <div
                      className={`${styles.progress} ${student.status === 'Ativo' ? styles.active : styles.inactive}`}
                      style={{ width: student.frequency }}
                    ></div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
};

export default Students;
