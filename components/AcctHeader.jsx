import { StyleSheet, Text, View, Image } from 'react-native';
import React from 'react';

const AcctHeader = () => {
  const name = 'John Smith';
  const email = 'johnsmith@gmail.com';
  return (
    <View>
      <View style={styles.userImg}>
        <Image 
          source={require('../assets/Avatar.png')}
          style={{width: 120, height: 120, borderRadius: 150 / 2,}}
        />
      </View>

      <View style={styles.header}>
        <Text style={styles.name}>{name}</Text>
        <Text style={styles.email}>{email}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  header: {
    alignItems: 'flex-end',
  },
  name: {
    fontSize: 56,
    fontWeight: 'bold',
  },
  email: {
    fontSize: 36,
    fontWeight: 'bold',
  },
  userImg: {
    marginLeft: 30,
    marginRight: 30,
    overflow: "hidden",
  }
});

export default AcctHeader;