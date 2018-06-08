using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class ButtonManager : MonoBehaviour {

	public void Button_Click()
    {
        SceneManager.LoadScene("Einhert_Start");
    }
}
