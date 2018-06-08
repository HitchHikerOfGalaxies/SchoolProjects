using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Player_Health : MonoBehaviour {

    public int health;

	// Use this for initialization
	void Start () {
	}
	
	// Update is called once per frame
	void Update () {
		if (gameObject.transform.position.y < -7) //gameObject being our player and if he falls below position y = -7 they die
        {
         Die();         
        }
    }
   void Die() //IEnumerator are the methods of this language which need a return value while void is a method with no return value
    {
        SceneManager.LoadScene("SampleScene"); //Resets the level back to the beginning after dying
    }
}
