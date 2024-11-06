import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Image } from 'react-native';
import BottomNavigationBar from './components/BottomNavigationBar'

const LoginScreen = () => {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  

  const handleLogin = () => {
       console.log('Login efetuado com sucesso!');
  };

  return (
    <View style={styles.screen}> 
      <Image
          source={require('./assets/pixels.png')} 
          style={styles.pixels}
          resizeMode="contain"
        />   
    <View style={styles.container}>
      <Image
          source={require('./assets/logo.png')} 
          style={styles.logo}
          resizeMode="contain"
        />
      <Text style={[styles.title, { fontFamily: 'LeagueSpartan' }]}>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="E-mail"
        value={email}
        onChangeText={(text) => setEmail(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Senha"
        secureTextEntry
        value={senha}
        onChangeText={(text) => setSenha(text)}
      />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={[styles.buttonText, { fontFamily: 'LeagueSpartan' }]}>Entrar</Text>
      </TouchableOpacity>
      <Text style={[styles.forgotPassword, { fontFamily: 'LeagueSpartan' }]}>Esqueceu a senha?</Text>
    </View>
    <BottomNavigationBar/>
    </View>
  );
};

const styles = StyleSheet.create({
  screen: {
    marginEnd: 0,
    flex: 1,    
    alignItems: 'center',
    backgroundColor: '#1A3E78',
  },
   pixels: {
    position: 'fixed',
    margimTop: 0,
    marginBottom: 0,
    width: '100%',
    height: 250,     
     
  },
  container: {   
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
    borderRadius: 20,
    width: 327,
    maxHeight: 435,
  },
   logo: {
    width: 268,
    height: 123,
    marginBottom: 10,
  },
  title: {
    color: '#FFCC10',
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    fontFamily: 'LeagueSpartan',
  },
  input: {
    width: 268,
    height: 37.5,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 10,
    padding: 10,
    marginBottom: 20,
    backgroundColor: '#D2E0FB',
    color: '#277BC0',
    fontFamily: 'LeagueSpartan',
  },
  button: {
    width: 240,
    height: 33,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#1A3E78',  
  },
  buttonText: {
    color: '#FFCC10',
    fontSize: 18,
    textAlign: 'center',
    fontFamily: 'LeagueSpartan',
  },
  forgotPassword: {
    fontSize: 16,
    color: '#1A3E78',
    marginTop: 20,
    fontFamily: 'LeagueSpartan',
  },
});

export default LoginScreen;